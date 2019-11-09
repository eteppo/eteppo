// allow direct use of programs (types) in two libraries (namespaces)
using Microsoft.ML.Probabilistic.Models;
using Microsoft.ML.Probabilistic.Distributions;
// all code must be organized into "namespaces" in c sharp
namespace csharp {
  // ... and classes
  class Program {
    // static makes Main method belong to Program class, not its particular instance
    // void means no return value
    // Main is run when file is run
    // string[] defines text array data structure
    static void Main(string[] args) {
      // angle bracket syntax is called generics
      // generics help write classes/methods that work with any data type
      // new keyword creates an object of supplied class (runs constructor)
      // observe boolean data of class VariableArray for treatment and control group
      VariableArray<bool> controlGroup = Variable.Observed(new bool[] { false, false, true, false, false });
      VariableArray<bool> treatedGroup = Variable.Observed(new bool[] { true, false, true, true, true });
      // indeces for patients in both groups of class Range
      Range i = controlGroup.Range; 
      Range j = treatedGroup.Range;
      // assume 50% probability for treatment being effective before data
      Variable<bool> isEffective = Variable.Bernoulli(0.5);
      // pre-declare probability of good outcome for both groups
      Variable<double> probIfTreated, probIfControl;
      // "using" defines scope at the end of which object is disposed
      // if treatment is effective, different probabilities of good outcome
      using (Variable.If(isEffective)) {
        // assume probability of good outcome Beta(1, 1) before data
        probIfControl = Variable.Beta(1, 1);  
        probIfTreated = Variable.Beta(1, 1);  
        // each patient gets true/false with that probability
        // "array[index] = value" assigns value to position index in array
        controlGroup[i] = Variable.Bernoulli(probIfControl).ForEach(i);  
        treatedGroup[j] = Variable.Bernoulli(probIfTreated).ForEach(j);  
      }
      // if treatment not effective, same probability of good outcome
      using (Variable.IfNot(isEffective)) {
        // assume probability of good outcome Beta(1, 1) before data
        Variable<double> probAll = Variable.Beta(1, 1);
        controlGroup[i] = Variable.Bernoulli(probAll).ForEach(i);  
        treatedGroup[j] = Variable.Bernoulli(probAll).ForEach(j);  
      }
      // get instance of class InferenceEngine for learning from data
      InferenceEngine ie = new InferenceEngine();
      // Infer returns input variable after observing data
      string effect = ie.Infer(isEffective).ToString();
      // mean of beta distribution is the most probable probability
      float treated = (float)ie.Infer<Beta>(probIfTreated).GetMean();
      float control = (float)ie.Infer<Beta>(probIfControl).GetMean();
      // output to results to console with WriteLine from System.Console
      System.Console.WriteLine("Probability of effect = " + effect);
      System.Console.WriteLine("Probability of good outcome if treatment = " + treated);  
      System.Console.WriteLine("Probability of good outcome if control = " + control);
    }
  }
}
// build and run with .NET dotnet command line utility
// 1. dotnet new console (create new console app project folder)
// 2. dotnet add package Microsoft.ML.Probabilistic.{Models, Compiler, Learners}
// 3. write current .cs file to that folder
// 4. dotnet run (in project folder) 
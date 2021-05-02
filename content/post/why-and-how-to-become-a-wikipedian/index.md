+++
title = "Why and How to Become a Wikipedian"
date = "2019-12-17"
+++

## Everything you need to know about editing Wikipedia

### 1. Check out Wikimedia projects

The movement behind Wikipedia is called the [Wikimedia](https://www.wikimedia.org/). Other Wikimedia's projects that you should consider checking out and contributing to include the [Wikibooks](https://www.wikibooks.org/) project.

### 2. Understand the URLs

All languages have their own main sites, e.g., the English Wikipedia is at [en.wikipedia.org](https://en.wikipedia.org/) and the Finnish at [fi.wikipedia.org](https://fi.wikipedia.org/). The articles are defined in the URL by title, like [en.wikipedia.org/wiki/Ageing](https://en.wikipedia.org/wiki/Ageing/). Since ageing can be an ambiguous term, people have made a so-called _disambiguation_ article to [en.wikipedia.org/wiki/Ageing_(disambiguation)](https://en.wikipedia.org/wiki/Ageing_(disambiguation)). In fact, the _Ageing_ article could be renamed to _Ageing (biology)_.

### 3. Understand Namespaces and read Metapages

Pages like [en.wikipedia.org/wiki/Wikipedia:Contributing_to_Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Contributing_to_Wikipedia) and [en.wikipedia.org/wiki/Help:Directory](https://en.wikipedia.org/wiki/Help:Directory) from the _Wikipedia_ and _Help_ namespaces include metainformation. At this point you should glance over those resources to see what other wikipedians expect from you (not a lot, they just want you to edit).

Similarly, Category pages, [en.wikipedia.org/wiki/Category:Clinical\_Medicine](https://en.wikipedia.org/wiki/Category:Clinical_Medicine) from the _Category_ namespace, include a tree of categories where people can find all articles related to a particular high-level topic. Improving the categorizations is also worth a lot of work since people can then use these categories as curricula to study particular fields of knowledge very easily.

User pages such as _en.wikipedia.org/wiki/User:User_ refer to pages describing user accounts. It's a good place to leave some information about your area of expertise right at the start.

Talk pages, like [en.wikipedia.org/wiki/Talk:Ageing](https://en.wikipedia.org/wiki/Talk:Ageing), link to the discussion page of the article. It's a good place to leave feedback and resolve editing conflicts. Similarly, the user account's Talk page is a good place to leave feedback for a user.

Finally, Template pages, like [en.wikipedia.org/wiki/Template:Reflist](https://en.wikipedia.org/wiki/Template:Reflist) contain templates that help organize and create structured information like references and infoboxes to the articles. You'll learn the most important ones by reading any good articles' Wikitext source. You can see message templates at [Wikipedia:Template\_messages](https://en.wikipedia.org/wiki/Wikipedia:Template_messages) and citation templates at [Wikipedia:Citation\_templates](https://en.wikipedia.org/wiki/Wikipedia:Citation_templates).

### 4. Wikitext

You can edit articles by using the visual interface but I recommend taking some time to learn _Wikitext_ or [Wiki markup language](https://en.wikipedia.org/wiki/Help:Cheatsheet). It lets you write, copy, save, and paste text easily since it's just raw text that the [MediaWiki software](https://www.mediawiki.org/wiki/MediaWiki) renders as articles. Also, using Wikitext directly helps you understand how links, citations, images, and so on and thus modify everything more easily.

I recommend to edit articles with a raw text editor, like [Sublime](https://www.sublimetext.com/). Copy and paste the raw _Wikitext_ to the text field in the _Edit source_ tab and preview to see how the raw text looks like rendered.

Here's almost everything you need to know about _Wikitext_ syntax to get started:

* Emphasis: `''italics''` and `'''bold'''`.
* Titles: `==Title==` the highest level title in the article and `===Subtitle===` is one level lower, and so on.
* `*` and `#` make bulleted and numbered lists. Use them with care.
* Citations:
	* It's best to use the Wikipedia's reference templates so that the reference list becomes more structured.
	* `<ref name="hello123">Someone et al. Title. Journal 12;345-5445.</ref>` adds a reference to the given journal article. The name attribute lets you reference the same citation with just `<ref name="hello123"/>`
	* `{{reflist}}` at the standard spot at the bottomm of the article tells the MediaWiki software to place the list of reference (as marked up with the `<ref>`-tags) there.
* Links:
	* `[[Title]]`: clicking _Title_ links to article _Title_.
	* `[[Title|pages]]`: clicking _pages_ links to article _Title_.
	* `[[Title#Subtitle|Subsection]]`: clicking _Subsection_ links to _Subtitle_ in article _Title_.
* Images: `[[File:filename.png|thumb|Caption]]` adds the file that has been previously uploaded to Wikipedia. Search for _Wikipedia extended image syntax_ when you need more settings.
* Categorization: `[[Category:Name]]` adds the page to _Category:Name_. It is usually placed at the bottom of the article's Wikitext.
* Messages: `{{cn}}` is the famous _[citation needed]_ tag that you can add after a claim that lacks a reference. See _Wikipedia:Template\_messages_ for all message templates.
* Redirection: `#REDIRECT [[Target page]]` redirects automatically to the article _Target page_. Use the visual interface for transfering pages; it handles the links correctly.
* Anything else: Search for the relevant help page if you want to make fancier things like tables and quotes.

### 5. Sandboxing

When you have an account, go to [Wikipedia:Sandbox](https://en.wikipedia.org/wiki/Wikipedia:Sandbox) and try everything.

## Why you should become a wikipedian

Knowledge moves our world forward. While there are many obstacles in the path to getting accurate knowledge (true justified beliefs) from low-level sources like scientific articles to the minds and actions of the people, one of the most important factors is accessibility.

Wikipedia is the most used source of high-level, textbook-like information on any imagineable topic. Whatever is your personal field of expertise and whatever are the authorative sources in your field, most people probably learn about those topics from Wikipedia. Increasingly also professionals seek high-level views about topics from Wikipedia. The best articles can be actually the best and most comprehensive review of the topic.

When you go and read about the topics of your expertise from Wikipedia, you'll very likely see that the articles are not good. For smaller languages, the articles probably don't even exist.

What might be the effects of people being able to learn more about the things that you know about? Experts need to learn to resist their harmful gatekeeping incentives and realize that the openness also creates a positive force for the experts to improve and provide more value to the world – instead of just blocking access to lower levels of value.

Editing Wikipedia is volunteering but there's a lot you get from it too. Many use editing as a learning tool; when you're forced to read, fix, and summarize some material, you tend to learn it better yourself. By checking sources and their validity and reliability you get to develop your critical thinking skills, and by writing educational content you get to practice your pedagogical writing skills.

If you're a teacher, a scientist, and so on, it could be claimed that part of your professional responsibilities is to educate the public. Editing Wikipedia – the number one encyclopedia of the world – is a big part of that. Instead of writing a closed pricey book, you should consider writing free open materials and use them in your teaching. You'll have a lot more success.

Wikipedia has been built by countless volunteers for all of humanity to benefit from. Open-source development by large communities in general is extremely effective and is slowly making for-profit information industries obsolete as we go deeper into the information age.

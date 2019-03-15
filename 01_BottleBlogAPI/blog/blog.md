---
title: A blog post on Markdown
date: 2019-03-15
author: SolarLiner
categories: blog,post,markdown
summary: We have here a simple Markdown file that is written by the author
series:
  id: example
  next: blog-2
---

This blog post will serve as example for the livestream. I need to fill in some kind of contents,
therefore here's an exerpt of the [Wikipedia article on Markdown](https://en.wikipedia.org/wiki/Markdown).

# Markdown

Markdown is a lightweight markup language with plain text formatting syntax. Its design allows it
to be converted to many output formats, but the original tool by the same name only supports HTML.
Markdown is often used to format readme files, for writing messages in online discussion forums,
and to create rich text using a plain text editor.

Since the initial description of Markdown contained ambiguities and unanswered questions, the
implementations that appeared over the years have subtle differences and many come with syntax
extensions.

## History

John Gruber created the Markdown language in 2004 in collaboration with Aaron Swartz on the syntax, with the goal of enabling people "to write using an easy-to-read and easy-to-write plain text format, optionally convert it to structurally valid XHTML (or HTML)".

Its key design goal is readability – that the language be readable as-is, without looking like it has been marked up with tags or formatting instructions, unlike text formatted with a markup language, such as Rich Text Format (RTF) or HTML, which have obvious tags and formatting instructions. To this end, its main inspiration is the existing conventions for marking up plain text in email, though it also draws from earlier markup languages, notably setext, Textile, and reStructuredText.

Gruber wrote a Perl script, Markdown.pl, which converts marked-up text input to valid, well-formed XHTML or HTML and replaces angle brackets '<' '>' and ampersands '&' with their corresponding character entity references. It can be used as a standalone script, as a plugin for Blosxom or Movable Type, or as a text filter for BBEdit.

Markdown has since been re-implemented by others e.g. in a Perl module available on CPAN (Text::Markdown), and in a variety of other programming languages. It is distributed under a BSD-style license and is included with, or available as a plugin for, several content-management systems.

Sites like GitHub, Bitbucket, Reddit, Diaspora, Stack Exchange, OpenStreetMap, and SourceForge use variants of Markdown to facilitate discussion between users.

### Standardization

Markdown has been characterised by an informal specification and a reference implementation for conversion to HTML. Over time, many Markdown implementations have appeared. People developed these mostly driven by the need for additional features on top of the base syntax—such as tables, footnotes, definition lists (technically HTML description lists), and Markdown inside HTML blocks. The behavior of some of these diverges from the reference implementation. At the same time, a number of ambiguities in the informal specification have attracted attention. These issues spurred an effort by some developers of Markdown parsers for standardisation.

Babelmark  is a tool available to "compare the output of various implementations" to "promote discussion of how and whether certain vague aspects of the markdown spec should be clarified." Gruber has argued that complete standardization would be mistaken: "Different sites (and people) have different needs. No one syntax would make all happy."

In March 2016 RFC 7763 and RFC 7764 were published. RFC 7763 introduced MIME type text/markdown with the original variant. RFC 7764 discusses and registered the variants MultiMarkdown, GitHub Flavored Markdown (GFM), Pandoc, CommonMark, and Markdown Extra among others.

### CommonMark

From 2012, a group of people including Jeff Atwood and John MacFarlane launched what Atwood characterized as a standardization effort. A community website now aims to "document various tools and resources available to document authors and developers, as well as implementors of the various markdown implementations". In September 2014, Gruber objected to the usage of "Markdown" in the name of this effort and it was rebranded as a new dialect named CommonMark. CommonMark.org published several versions of a specification, reference implementation, and test suite, and "plans to announce a finalized 1.0 spec and test suite in 2018."

### GFM

In 2017, GitHub released a formal specification of their GitHub Flavored Markdown (GFM) that is based on CommonMark. It follows the CommonMark specification exactly except for tables, strikethrough, autolinks and task lists, which the GitHub spec has added as extensions. GitHub also changed the parser used on their sites accordingly, which required that some documents be changed — for instance, GFM now requires that the hash symbol that creates a heading is separated by a space character.

Markdown Extra is a lightweight markup language based on Markdown implemented in PHP (originally), Python and Ruby. It adds features not available with plain Markdown syntax. Markdown Extra is supported in content management systems, for example Drupal, TYPO3 and MediaWiki.

It adds the following features to Markdown:

- markdown markup inside HTML blocks
- elements with id/class attribute
- fenced code blocks
- tables 
- definition lists
- footnotes
- abbreviations
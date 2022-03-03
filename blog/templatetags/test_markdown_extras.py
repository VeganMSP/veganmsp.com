from django.test import TestCase

from .markdown_extras import markdown


class MarkdownTestCase(TestCase):
    def test_markdown(self):
        markdown_text = """# This is a heading.

Here we have a paragraph. It's just two lines.[^1]

```python
import django
```

That was a code block.

[^1]: Depends on how you count, I guess."""
        expected_value = """<h1 id="this-is-a-heading">This is a heading.</h1>

<p>Here we have a paragraph. It's just two lines.<sup class="footnote-ref" id="fnref-1"><a href="#fn-1">1</a></sup></p>

<pre><code>import django
</code></pre>

<p>That was a code block.</p>

<div class="footnotes">
<hr />
<ol>
<li id="fn-1">
<p>Depends on how you count, I guess.&#160;<a href="#fnref-1" class="footnoteBackLink" title="Jump back to footnote 1 in the text.">&#8617;</a></p>
</li>
</ol>
</div>
"""
        self.assertEqual(markdown(markdown_text), expected_value)

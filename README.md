# pastepy
Supposed to be a Module but im to dumb to figure that out...
Please don't steal ._.
## How to use
Put the pastepy.py File in your Project then import it:
`import pastepy`
## Create new Paste
To create a new PasteBin:
`pastepy.new(key, title, content, language)`
If API Request is successful, it will return the Link
## Examples
Here is an Example, which creates a Hello World Python Paste:
```python
import pastepy

paste = pastepy.new("INSERT KEY HERE", "Hello World in Python", 'print("Hello World")', "python")

print(paste)
```

Example Output:
```
https://pastebin.com/affZakP8
```
## Developer Key
To get your API Key, log into Pastebin, then go to:
https://pastebin.com/doc_api
Scroll down to "Your Unique Developer API Key" and copy it.
It is only visible for logged in Users.

### Plugin: japanese
This plugin is intended to provide random japanese words as well as their translations

#### Routes

| route             | action |
| -----             | ------ |
| /japanese         | return a random index between 0 and the max number of entries in the word list |
| /japanese/index   | return the word at the given index, as well as its translation and any notes |
| /japanese/index/0 | return the word at the given index |
| /japanese/index/1 | return the notes for the word at the given index |
| /japanese/index/2 | return the translation for the word at the given index |


#### Intended Use
The intended use would be to query /japanese, receive the index of the word, and then follow up with three queries for the word itself, the notes, and the answer as needed by the querying application


#### Word List Format
The word list is in wordlist.txt, and each entry is on its own line of the following format:
```
japanese word – definition in english (any other notes about it)
```
The important parts being the em-dash (–) and the parentheses. Category lines are ignored.

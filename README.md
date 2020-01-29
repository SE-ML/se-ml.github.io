# se-ml.github.io

Software Engineering for Machine Learning Lab Homepage


### Prereq
Install (jekyll and bundler)[https://jekyllrb.com/docs/].

### Development:

#### Install dependencies:
```
$ git clone https://github.com/SE-ML/se-ml.github.io
$ cd se-ml.github.io
$ git fetch --all
$ git checkout -b source origin/source
$ bundle install
```

#### Run dev server:
```
$ bundle exec jekyll serve
```

### Deploy to production:
```
$ ./bin/deploy se-ml
```


#### Thanks to:
- this webpage uses the [al-folio](https://alshedivat.github.io/al-folio/) theme.

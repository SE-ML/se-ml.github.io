# se-ml.github.io

> Software Engineering for Machine Learning Homepage

### Prerequisites

Install [jekyll](https://jekyllrb.com/docs/).

### Development:

#### Install dependencies

```sh
$ git clone https://github.com/SE-ML/se-ml.github.io
$ cd se-ml.github.io
$ git fetch --all
$ git checkout -b source origin/source
$ bundle install
```

#### Run development server

```sh
bundle exec jekyll serve --incremental
```
> The website will be available at [localhost:4000](http://localhost:4000)

### Deploy to production

```sh
$ ./bin/deploy -u se-ml
```

#### Kudos

- this webpage uses the [al-folio](https://alshedivat.github.io/al-folio/) theme.
- some icons are downloaded from [Freepik](https://www.freepik.com/).

Thank you!

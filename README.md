BBCT API
=

![Tests](https://github.com/BaseballCardTracker/bbct-api/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/BaseballCardTracker/bbct-api/branch/master/graph/badge.svg?token=E4I3IK3VYP)](https://codecov.io/gh/BaseballCardTracker/bbct-api)
![CodeQL](https://github.com/BaseballCardTracker/bbct-api/actions/workflows/codeql-analysis.yml/badge.svg)

This is a REST API for BBCT.

Environment Variables
=

Create a file named `.env` and set these variables:

* `DJANGO_SECRET_KEY`
* `DJANGO_ALLOWED_HOSTS`
* `DJANGO_DEBUG` - optional
* `DB_ENGINE`
* `DB_HOST`
* `DB_PORT`
* `DB_USER`
* `DB_PASSWORD`
* `DB_NAME`
* `GOOGLE_OAUTH2_CLIENT_ID` - See https://developers.google.com/workspace/guides/create-credentials#oauth-client-id
* `GOOGLE_OAUTH2_CLIENT_SECRET`

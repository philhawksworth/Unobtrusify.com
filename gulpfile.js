var gulp = require('gulp');
var shell = require('gulp-shell');

// deploy to gh-pages.
gulp.task('deploy', shell.task([
  'git subtree push --prefix dist origin gh-pages'
]));

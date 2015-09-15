var gulp         = require('gulp')
var less         = require('gulp-less')
var autoprefixer = require('gulp-autoprefixer')
var sourcemaps   = require('gulp-sourcemaps')

gulp.task('less', function() {
  gulp.src('app/core/static/less/main.less')
    .pipe(sourcemaps.init())
    .pipe(less())
    .pipe(autoprefixer())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('app/core/static/css'))
})

gulp.task('less:watch', function () {
  gulp.watch('app/core/static/less/*.less', ['less'])
})

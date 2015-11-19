var gulp         = require('gulp')
var sass         = require('gulp-sass')
var autoprefixer = require('gulp-autoprefixer')
var sourcemaps   = require('gulp-sourcemaps')

gulp.task('sass', function() {
  gulp.src('app/core/static/sass/app.sass')
    .pipe(sourcemaps.init())
    .pipe(sass())
    .pipe(autoprefixer())
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('app/core/static/css'))
})

gulp.task('sass:watch', function () {
  gulp.watch('app/core/static/sass/*.sass', ['sass'])
})

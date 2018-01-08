jQuery(function($) {
  'use strict'

  $('.add-popover').each(function() {
    $(this).popover({ container: 'body', html: true })
  })
})

function qpsToString(qps) {
  return Object.keys(qps)
    .reduce(function(arr, key) {
      if (qps[key]) {
        arr.push(key + '=' + qps[key])
      }

      return arr
    }, [])
    .join('&')
}

function getCurrentURLWithoutPage() {
  return location.href.replace(/&?page=\d+/, '')
}

Vue.component('candidate-pagination', {
  data: function() {
    return {
      url: getCurrentURLWithoutPage()
    }
  },
  computed: {
    baseUrl: function() {
      if (this.url.search(/\?/) === -1) {
        return this.url + '?'
      }

      return this.url + '&'
    },
    prevPage: function() {
      return this.page === 1 ? 1 : this.page - 1
    },
    nextPage: function() {
      return this.page < this.pages.length ? this.page + 1 : this.page
    },
    prevDisabled: function() {
      return this.prevPage === this.page
    },
    nextDisabled: function() {
      return this.nextPage === this.page
    }
  },
  template: `
    <nav class="text-center">
      <ul v-if="pages.length" class="pagination">
        <candidate-pagination-page :disabled="prevDisabled" content="«" :page="prevPage"></candidate-pagination-page>
        <candidate-pagination-page
          v-for="i in pages"
          :current="page"
          :content="i"
          :page="i"
          :key="i"
        >
        </candidate-pagination-page>
        <candidate-pagination-page :disabled="nextDisabled" content="»" :page="nextPage"></candidate-pagination-page>
      </ul>
    </nav>
  `,
  props: ['page', 'pages']
})

Vue.component('candidate-pagination-page', {
  computed: {
    base: function() {
      let url = getCurrentURLWithoutPage()

      if (url.search(/\?/) === -1) {
        return url + '?'
      }

      return url + '&'
    },
    url: function() {
      return this.base + 'page=' + this.page
    },
    active: function() {
      return parseInt(this.current) === parseInt(this.page)
    }
  },
  template: `
    <li :class="{ active: active, disabled: disabled }">
      <a v-if="!disabled" :href="url">{{ content }}</a>
      <a v-else>{{ content }}</a>
    </li>
  `,
  props: ['page', 'current', 'content', 'disabled']
})

Vue.component('candidate-list', {
  template: `
    <table class="table table-striped">
      <tbody>
        <candidate-list-item
          v-for="candidate in candidates"
          :key="candidate.id"
          :candidate="candidate"
        ></candidate-list-item>
      </tbody>
    </table>
  `,
  props: ['candidates']
})

Vue.component('candidate-list-item', {
  template: `
    <tr>
      <td>
        <div class="row candidate-row">
          <div class="col-xs-12 col-md-5 col-sm-6 center-xs">
            <img v-if="candidate.thumbnail" class="img-thumbnail" width="60px" :src="candidate.thumbnail">
            <img v-else class="img-thumbnail" width="60px" src="/static/images/placeholder.svg">
            <br class="visible-xs">
            <a :href="candidate.profile_link">
              {{ candidate.first_name }} {{ candidate.last_name }}
              <span v-if="candidate.party_short !== '-' || candidate.state_name !== '-'">
                (<span v-if="candidate.party_short !== '-'">{{candidate.party_short}}</span><span v-if="candidate.party_short !== '-' && candidate.state_name !== '-'">, </span><span v-if="candidate.state_name !== '-'">{{candidate.state_name}}</span>)
              </span>
            </a>
          </div>
          <div class="col-xs-12 col-md-7 col-sm-6 charts">
            <div class="statistic" :id="'statistic-' + candidate.id"></div>
            <div class="detail" :id="'detail-' + candidate.id"></div>
          </div>
        </div>
      </td>
    </tr>
  `,
  props: ['candidate'],
  mounted: function() {
    this.$nextTick(function() {
      let data = this.candidate.statistic
      let margin = data.summary.length > 1 ? 0 : 30

      $('#statistic-' + this.candidate.id).highcharts({
        chart: {
          type: 'bar',
          marginTop: margin / 2,
          marginBottom: margin / 2,
          backgroundColor: 'transparent',
          height: 60
        },
        title: null,
        xAxis: {
          categories: data.summary.map(function(sum) {
            return sum.title
          }),
          title: null
        },
        yAxis: {
          min: 0,
          max: 10,
          minorTickInterval: 1,
          title: null,
          labels: {
            enabled: false
          }
        },
        credits: {
          enabled: false
        },
        legend: {
          enabled: false
        },
        tooltip: false,
        plotOptions: {
          bar: {
            stacking: 'normal',
            pointWidth: 15
          },
          series: {
            point: {
              events: {
                click: function(e) {
                  let rect = $(this.graphic.element)
                  let charts = rect.closest('.charts')
                  let detail = charts.children('.detail')

                  let effect = 'drop'

                  $('.detail')
                    .not(detail)
                    .hide(effect)

                  detail.toggle(effect, function(e) {
                    window.dispatchEvent(new Event('resize'))
                  })
                }
              }
            }
          }
        },
        series: [
          {
            name: '',
            data: data.summary.map(function(sum) {
              return sum.value.negative
            }),
            color: '#990000'
          },
          {
            name: '',
            data: data.summary.map(function(sum) {
              return sum.value.positive
            }),
            color: '#009900'
          }
        ]
      })

      $('#detail-' + this.candidate.id).highcharts({
        chart: {
          type: 'bar',
          backgroundColor: 'transparent',
          height: data.detail.length * 25 + 20
        },
        title: {
          text: ' '
        },
        subtitle: {
          text: ' '
        },
        xAxis: {
          categories: data.detail.map(function(det) {
            return det.category
          })
        },
        credits: {
          enabled: false
        },
        yAxis: {
          min: 0,
          max: 10,
          title: ' ',
          minorTickInterval: 1,
          labels: {
            enabled: false
          }
        },
        tooltip: false,
        plotOptions: {
          column: {
            pointPadding: 0.2,
            borderWidth: 0
          },
          bar: {
            pointWidth: 15
          }
        },
        legend: {
          enabled: false
        },
        series: [
          {
            colorByPoint: true,
            minPointLength: 3,
            data: data.detail.map(function(det) {
              return det.value
            })
          }
        ]
      })
    })
  }
})

new Vue({
  el: '#vue-app',
  data: {
    limit: 10,
    results: []
  },
  computed: {
    page: function() {
      let page = location.search.match(/page=(\d+)/)

      return page ? parseInt(page[1]) : 1
    },
    candidates: function() {
      let end = this.page * this.limit

      return this.results.slice(end - this.limit, end)
    },
    pages: function() {
      return Array.from(
        { length: Math.ceil(this.results.length / this.limit) },
        function(_, k) {
          return k + 1
        }
      )
    }
  },
  mounted: function() {
    let state = location.search.match(/state=(\d+)/)
    let category = location.search.match(/category=(\d+)/)
    let search = location.search.match(/search=(\w+)/)
    let evaluate = location.search.match(/evaluate=(\d+)/)

    state = state ? parseInt(state[1]) : null
    category = category ? parseInt(category[1]) : null
    search = search ? search[1] : null
    evaluate = evaluate ? true : false

    fetch(
      '/api/v2/politicians/?' +
        qpsToString({
          state: state,
          category: category,
          search: search,
          evaluate: evaluate
        }),
      {
        headers: {
          'Accept-Language':
            document.querySelector('.language ul > li > a > strong').parentNode
              .dataset.lang || 'de'
        }
      }
    ).then(
      function(res) {
        res.json().then(
          function(data) {
            let i = category > 0 ? 1 : 0

            this.results = _.sortBy(data, [
              function(x) {
                return x.statistic.summary[i].value.negative
              },
              'first_name',
              'last_name'
            ])
          }.bind(this)
        )
      }.bind(this)
    )
  }
})

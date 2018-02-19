jQuery(function($) {
  'use strict'

  $('.add-popover').each(function() {
    $(this).popover({ container: 'body', html: true })
  })
})

function cleanParams(params) {
  return Object.keys(params).reduce(function(clean, key) {
    if (params[key]) {
      clean[key] = params[key]
    }

    return clean
  }, {})
}

Vue.component('loading-spinner', {
  template: `
    <div class="loading-wrapper">
      <div class="loading-spinner"></div>
    </div>
  `
})

Vue.component('candidate-pagination', {
  computed: {
    prevPage: function() {
      return parseInt(this.page) === 1 ? 1 : parseInt(this.page) - 1
    },
    nextPage: function() {
      return parseInt(this.page) < this.pages.length
        ? parseInt(this.page) + 1
        : parseInt(this.page)
    },
    prevDisabled: function() {
      return parseInt(this.prevPage) === parseInt(this.page)
    },
    nextDisabled: function() {
      return parseInt(this.nextPage) === parseInt(this.page)
    },
    count: function() {
      return interpolate(
        gettext('Candidates %(start)s to %(end)s of %(total)s'),
        {
          start: this.start,
          end: this.end,
          total: this.total
        },
        true
      )
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
      <div class="text-center">
        <em>
          {{ count }}
        </em>
      </div>
    </nav>
  `,
  props: ['page', 'pages', 'start', 'end', 'total']
})

Vue.component('candidate-pagination-page', {
  computed: {
    url: function() {
      let url = new URL(location)

      url.searchParams.delete('page')
      url.searchParams.append('page', this.page)

      return url
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
            <a :href="candidate.profile_link">
              <img v-if="candidate.thumbnail" class="img-thumbnail" :src="candidate.thumbnail">
              <img v-else class="img-thumbnail" src="/static/images/placeholder.svg">
            </a>
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
    results: [],
    loading: true
  },
  computed: {
    page: function() {
      return new URL(location).searchParams.get('page') || 1
    },
    candidates: function() {
      let end = this.page * this.limit

      return this.results.slice(end - this.limit, end)
    },
    pageStart: function() {
      return this.page * this.limit - this.limit + 1
    },
    pageEnd: function() {
      return this.pageStart - 1 + this.candidates.length
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
    let currentUrl = new URL(location)

    fetch(
      '/api/v2/politicians/?' +
        new URLSearchParams(
          cleanParams({
            state: parseInt(currentUrl.searchParams.get('state')),
            category: parseInt(currentUrl.searchParams.get('category')),
            search: currentUrl.searchParams.get('search'),
            evaluate: parseInt(currentUrl.searchParams.get('evaluate')),
            party: parseInt(currentUrl.searchParams.get('party')),
            is_member_of_parliament: parseInt(
              currentUrl.searchParams.get('is_member')
            )
          })
        ).toString(),
      {
        credentials: 'same-origin',
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
            let i = currentUrl.searchParams.get('category') > 0 ? 1 : 0

            this.results = _.sortBy(data, [
              function(x) {
                return x.statistic.summary[i].value.negative
              },
              'first_name',
              'last_name'
            ])

            this.loading = false
          }.bind(this)
        )
      }.bind(this)
    )
  }
})

import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import FullArticle from './views/FullArticle.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  hashbang: false,
  history: true,
  base: '/',
  routes: [
    {
      path: '*',
      name: 'home',
      component: Home
    },
    {
      path: '/full-article/:id',
      name: 'full-article',
      component: FullArticle,
      props: (route) => ({
        article: route.params.articleData
      }),
    }
  ]
})

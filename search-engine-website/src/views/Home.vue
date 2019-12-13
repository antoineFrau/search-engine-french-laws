<template>
  <div>
    <section class="hero is-small">
        <div class="hero-body">
            <div class="container" >
              <div class="columns is-vcentered">
                <b-field class="column">
                  <b-input
                      placeholder="Recherche..."
                      type="search"
                      size="is-large"
                      v-model="search"
                      icon="magnify"
                      @keydown.native.enter="searchLaws" 
                      rounded>
                  </b-input>
                </b-field>

                <a class="column is-1" v-on:click="this.showHideAll">
                  <span v-show="currentArticleListState" class="icon">
                    <i class="fas fa-angle-double-up"></i>
                  </span>
                  <span v-show="currentArticleListState === false" class="icon">
                    <i class="fas fa-angle-double-down"></i>
                  </span>
                </a>
              </div>
            </div>
        </div>
    </section>
    <section class="hero is-small">
      <div class="hero-body">
        <div class="container"></div>
      </div>
    </section>
    <section class="container">
      <Article
        v-for="law in laws"
        v-bind:key="law._source.articleId"
        :id="law._source.articleId"
        :esId="law._id"
        :text="law._source.articleText"
        :textHtml="law._source.articleTextHTML"
        :parents="law._source.listParentId"
        :kindOfLaw="findKindOfLaw(law._source.listParentId[0].parentId)"
        ref="article"
      />
    </section>
    <b-notification v-show="isLoading" :closable="false">
        <b-loading :is-full-page="true" :active.sync="isLoading" :can-cancel="false"></b-loading>
    </b-notification>
  </div>
</template>


<script>
import SearchService from '../services/SearchService'
import Article from '../components/Article'

export default {
  name: 'home',
  data: function () {
    return {
      search: '',
      laws: {},
      legislativeSearch: false,
      reglementaireSearch: false,
      annexeSearch: false,
      currentArticleListState: false,
      isLoading: false,
    }
  },
  methods: {
    searchLaws () {
      this.laws = []
      this.isLoading = true
      SearchService.searchLaws(this.search).then(r => {
        this.laws = r.data.hits.hits
        // setTimeout(() => {
        //     this.isLoading = false
        // }, 3 * 1000)
        this.isLoading = false
      })
    },
    findKindOfLaw (parentId) {
      switch (parentId) {
        case "LEGISCTA000006108136":
          return "Législative"
          break;
        case "LEGISCTA000006112857":
          return "Réglementaire"
          break;
        case "LEGISCTA000006108629":
          return "Annexe"
          break;
      }
    },
    showHideAll () {
      this.$refs.article.map(article => article.isOpen = (this.currentArticleListState))
      this.currentArticleListState = (!this.currentArticleListState)
    }
  },
  components: {
    Article
  },
}
</script>

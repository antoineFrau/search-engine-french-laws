<template>
  <div v-if="isPropsStillThere">
    <section class="hero is-primary is-medium is-bold">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="title"></h1>
        </div>
      </div>
    </section>
    <div class="container">
      <section class="articles">
          <div class="column is-10 is-offset-1">
              <div class="card article">
                  <div class="card-content">
                    <div class="media">
                        <div class="media-content has-text-centered">
                            <p class="title article-title">Article {{law.articleId}} - {{law.listParentId[0].parentTitle}}</p>
                            <div class="tags has-addons level-item">
                                <span class="tag is-rounded is-info">@DILA_officiel</span>
                                <span class="tag is-rounded">Dec 13 2019</span>
                            </div>
                        </div>
                    </div>
                    <div class="content article-body" v-html="law.articleTextHTML">
                        {{law.articleTextHTML}}
                    </div>
                    <div class="media">
                      <div class="media-content has-text-centered">
                        <div class="tags level-item">
                          <b-taglist>
                            <b-tag rounded v-for="parent in law.listParentId" v-bind:key="parent.parentId">{{
                              parent.parentTitle.includes(":") ? parent.parentTitle.split(":")[0] : parent.parentTitle
                              }}</b-tag>
                          </b-taglist>
                        </div>
                      </div>
                    </div>
                  </div>
              </div>
          </div>
      </section>
    </div>
    <b-notification v-show="isLoading" :closable="false">
        <b-loading :is-full-page="true" :active.sync="isLoading" :can-cancel="false"></b-loading>
    </b-notification>
  </div>
</template>


<script>
import SearchService from '../services/SearchService'
export default {
  name: 'full-article',
  props: ["article"],
  data: function () {
    return {
      law: {},
      isLoading: false
    }
  },
  computed: {
    isPropsStillThere () {
      if (this.props === undefined && Object.entries(this.law).length === 0 && this.law.constructor === Object) {
        let id = this.$route.params["id"]
        this.isLoading = true
        SearchService.getArticleById(id).then(r => {
          if (!r.data.found) {
            this.$router.push('')
            return false
          }
          this.law = r.data._source
          this.isLoading = false
        })
      } else if (Object.entries(this.law).length === 0 && this.law.constructor === Object) {
        this.law = this.props.article
      }
      return true
    }
  },
  methods: {
    findKindOfLaw (parentId) {
      switch (parentId[0]) {
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
    }
  }
}
</script>
<style scoped>
.articles {
  margin: 5rem 0;
  margin-top: -200px;
}
.articles .content p {
    line-height: 1.9;
    margin: 15px 0;
}
.author-image {
    position: absolute;
    top: -30px;
    left: 50%;
    width: 60px;
    height: 60px;
    margin-left: -30px;
    border: 3px solid #ccc;
    border-radius: 50%;
}
.media-center {
  display: block;
  margin-bottom: 1rem;
}
.media-content {
  margin-top: 3rem;
}
.article, .promo-block {
  margin-top: 6rem;
}
div.column.is-8:first-child {
  padding-top: 0;
  margin-top: 0;
}
.article-title {
  font-size: 2rem;
  font-weight: lighter;
  line-height: 2;
}
.article-subtitle {
  color: #909AA0;
  margin-bottom: 3rem;
}
.article-body {
  line-height: 1.4;
  margin: 0 6rem;
}
.promo-block .container {
  margin: 1rem 5rem;
}
</style>
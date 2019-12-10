<template>
  <div class="columns is-centered">
    <div class="column is-three-quarters">
      <div class="card">
        <header class="card-header">
          <div class="card-header-title">
            <div class="columns is-gapless">
              <div class="column"><p>Article #{{id}}</p></div>
              <div class="column is-2">
                <span v-if="kindOfLaw == 'Législative'" class="tag is-primary">{{kindOfLaw}}</span>
                <span v-if="kindOfLaw == 'Réglementaire'" class="tag is-dark">{{kindOfLaw}}</span>
                <span v-if="kindOfLaw == 'Annexe'" class="tag is-info">{{kindOfLaw}}</span>
              </div>
            </div>
          </div>
           
          <a v-on:click="hideArticle" class="card-header-icon" aria-label="more options">
            <span v-show="isOpen" class="icon">
              <i class="fas fa-angle-down"></i>
            </span>
            <span v-show="isOpen === false" class="icon">
              <i class="fas fa-angle-up"></i>
            </span>
          </a>
        </header>
        <div class="card-content" v-if="isOpen">
          <div class="content" v-html="textHtml">
            {{ textHtml }}
          </div>
        </div>
        <footer class="card-footer" v-if="isOpen">
          <a href="#" class="card-footer-item">Enregistrer</a>
          <a href="#" class="card-footer-item">Copier</a>
          <a href="#" class="card-footer-item">Partager</a>
        </footer>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'article',
  data: function () {
    return {
      isOpen: true
    }
  },
  props: ["text", "textHtml", "id", "parentIds", "kindOfLaw"],
  methods: {
    hideArticle () {
      this.isOpen = (!this.isOpen)
    }
  }
}
// # note : 
// # - LEGISCTA000006108136 -> legislative
// # - LEGISCTA000006112857 -> reglementaire
// # - LEGISCTA000006108629 -> annexe
</script>

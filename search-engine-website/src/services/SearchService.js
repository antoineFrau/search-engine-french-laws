import Api from '@/services/Api'

export default {
  searchLaws(term) {
    return Api().get("_search?q=" + term);
  }
//   searchLegiLaws(term) {
//     return Api().get("/q=" + term);
//   },
//   searchReglementaryLaws(term) {
//     return Api().get("/q=" + term);
//   },
//   searchAnexLaws(term) {
//     return Api().get("/q=" + term);
//   }
};
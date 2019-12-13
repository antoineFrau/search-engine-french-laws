import axios from 'axios'

export default() => {
    return axios.create({
      baseURL: `http://localhost:9200/laws-all-with-title`,
      withCredentials: false,
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    });
}
import axios from 'axios'

export default() => {
    return axios.create({
      baseURL: `http://localhost:9200/laws-all`,
      withCredentials: false,
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      }
    });
}
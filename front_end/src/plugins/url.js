import axios from "axios";

const api = axios.create({
 baseURL: "http://localhost:1600",
});

export default api;
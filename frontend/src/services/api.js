import axios from "axios";

const API = axios.create({
  baseURL: "https://leaddesk-mini-production-9913.up.railway.app",
});

export default API;
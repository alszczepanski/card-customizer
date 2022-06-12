import axios from "axios";

import { getItem } from "./services/localstorage";

const BASE_URL = "http://localhost:8000";

const api = axios.create({
    baseURL: BASE_URL,
    headers: {
        "Content-Type": "application/json"
    }
  });

api.interceptors.request.use((config) => {
    const token = getItem("cards-auth-token");
    config.headers.Authorization =  `Bearer ${token}`;
    return config;
  }, function (error) {
    return Promise.reject(error);
  });

export default api;
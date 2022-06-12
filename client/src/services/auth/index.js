import api from "@/api";

export const login = ({ username, password }) =>
  api.post("/login", { username, password });

export const register = ({ username, password }) =>
  api.post("/register", { username, password });

export const restoreUser = () => api.get("/users/me");
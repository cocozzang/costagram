import { createStore } from "vuex";

export default createStore({
  state: {
    isAuthenticated: false,
    token: "",
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
});

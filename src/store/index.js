import { createStore } from "vuex";
import createPersistedState from "vuex-persistedstate";

export default createStore({
  state: {
    isAuthenticated: false,
    token: "",
    userInfo: {
      id: "",
      username: "",
      nickname: "",
      profile_thumbnail: "",
    },
  },
  getters: {},
  mutations: {
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
    setUserInfo(state, { id, username, nickname, profile_thumbnail }) {
      state.userInfo.id = id;
      state.userInfo.username = username;
      state.userInfo.nickname = nickname;
      state.userInfo.profile_thumbnail = profile_thumbnail;
    },
    removeUserInfo(state) {
      state.userInfo.id = "";
      state.userInfo.username = "";
      state.userInfo.nickname = "";
      state.userInfo.profile_thumbnail = "";
    },
  },
  actions: {},
  modules: {},
  plugins: [createPersistedState()],
});

import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "FeedView",
    component: () =>
      import(/* webpackChunkName: "feed" */ "@/views/FeedView.vue"),
  },
  {
    path: "/login",
    name: "LoginView",
    component: () =>
      import(/* webpackChunkName: "login" */ "@/views/LoginView.vue"),
  },
  {
    path: "/profile",
    name: "ProfileView",
    component: () =>
      import(/* webpackChunkName: "login" */ "@/views/ProfileView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () =>
      import(
        /* webpackChunkName: "layouts-default-index" */
        "@/layouts/default/Index.vue"
      ),
    children: [
      {
        path: "",
        name: "FeedView",
        component: () =>
          import(/* webpackChunkName: "feed" */ "@/views/FeedView.vue"),
      },
      {
        path: "profile",
        name: "ProfileView",
        component: () =>
          import(/* webpackChunkName: "login" */ "@/views/ProfileView.vue"),
      },
    ],
  },
  {
    path: "/authentication",
    component: () =>
      import(
        /* webpackChunkName: "layouts-default-login" */
        "@/layouts/authentication/Index"
      ),
    children: [
      {
        path: "log-in",
        name: "LoginView",
        component: () =>
          import(/* webpackChunkName: "views-login" */ "@/views/LoginView"),
      },
      {
        path: "sign-up",
        name: "SignupView",
        component: () =>
          import(/* webpackChunkName: "views-signup" */ "@/views/SignupView"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

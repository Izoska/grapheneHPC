import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import LikeStock from "../views/LikeStock.vue";
import MyStock from "../views/MyStock.vue";
import TodayIssue from "../views/TodayIssue.vue";
import User from "../views/User.vue";
import StockDetail from "../views/StockDetail.vue";
import Popup from "../views/Popup.vue";
import UserLogin from "@/components/userinfo/UserLogin.vue";
import UserUpdate from "@/components/userinfo/UserUpdate.vue";
import UserJoin from "@/components/userinfo/UserJoin.vue";
import UserPassword from "@/components/userinfo/UserPassword.vue";
import ListStock from "../views/ListStock.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/likestock",
    name: "LikeStock",
    component: LikeStock,
  },
  {
    path: "/mystock",
    name: "MyStock",
    component: MyStock,
  },
  {
    path: "/list",
    name: "ListStock",
    component: ListStock,
  },
  {
    path: "/todayissue",
    name: "TodayIssue",
    component: TodayIssue,
  },
  {
    path: "/detail/:id",
    name: "StockDetail",
    component: StockDetail,
  },
  {
    path: "/popup",
    name: "Popup",
    component: Popup,
  },
  {
    path: "/member",
    name: "User",
    component: User,
    children: [
      {
        path: "login",
        name: "UserLogin",
        component: UserLogin,
      },
      {
        path: "update",
        name: "UserUpdate",
        component: UserUpdate,
      },
      {
        path: "Join",
        name: "UserJoin",
        component: UserJoin,
      },
      {
        path: "password",
        name: "UserPassword",
        component: UserPassword,
      },
    ],
  },
];

const router = new VueRouter({
  mode:'history',
  routes,
});

export default router;

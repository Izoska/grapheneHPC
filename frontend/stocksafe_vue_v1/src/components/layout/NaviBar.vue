
<template>
  <!-- Sidebar -->
  <ul
    class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion ml-2"
    id="accordionSidebar"
  >
    <!-- Sidebar - Brand -->
    <!-- <a
      class="sidebar-brand d-flex align-items-center justify-content-center"
      href="index.html"
    > -->
    <div class="sidebar-brand-icon rotate-n-15">
      <i class="fas fa-laugh-wink"></i>
    </div>
    <div class="sidebar-brand-text mx-3">
      <router-link
        class="
          homelogo
          align-items-center
          justify-content-center
          sidebar-brand
          d-flex
        "
        to="/"
      >
        Stock Safe
      </router-link>
    </div>
    <!-- </a> -->

    <!-- Divider -->
    <hr class="sidebar-divider" />

    <!-- Heading -->
    <div class="sidebar-heading">시장</div>

    <!-- Nav Item - Utilities Collapse Menu -->
    <li class="nav-item">
      <router-link class="ll" :to="{ name: 'TodayIssue' }"
        >오늘의 이슈</router-link
      >
    </li>

    <!-- Divider -->
    <hr class="sidebar-divider" v-if="this.getLoginState" />

    <!-- Heading -->
    <div class="sidebar-heading" v-if="this.getLoginState">자산관리</div>

    <!-- Nav Item - Pages Collapse Menu -->
    <li class="nav-item" v-if="this.getLoginState">
      <router-link class="ll" :to="{ name: 'MyStock' }">내 주식</router-link>
    </li>

    <!-- Nav Item - Charts -->
    <li class="nav-item" v-if="this.getLoginState">
      <router-link class="ll" :to="{ name: 'LikeStock' }">관심주식</router-link>
    </li>

    <!-- Nav Item - Charts -->
    <li class="nav-item" v-if="this.getLoginState">
      <router-link class="ll" :to="{ name: 'ListStock', query: { list: all } }"
        >주식목록</router-link
      >
    </li>

    <!-- Divider -->
    <hr class="sidebar-divider d-none d-md-block" />
    <div v-if="this.getLoginState">
      <div class="sidebar-heading">내 정보 관리</div>

      <!-- Nav Item - Pages Collapse Menu -->
      <li class="nav-item">
        <i class="bi bi-arrow-clockwise"></i>
        <router-link class="ll" :to="{ name: 'UserUpdate' }">
          <!-- <b-icon-exclamation-triangle-fill></b-icon-exclamation-triangle-fill>내 -->
          내 정보 수정/탈퇴</router-link
        >
      </li>

      <!-- Divider -->
      <hr class="sidebar-divider d-none d-md-block" />
    </div>

    <!-- Sidebar Toggler (Sidebar) -->
    <div class="text-center d-none d-md-inline">
      <button class="rounded-circle border-0" id="sidebarToggle"></button>
    </div>

    <!-- Sidebar Message -->
    <!-- <div class="sidebar-card d-none d-lg-flex">
      <img
        class="sidebar-card-illustration mb-2"
        src="img/undraw_rocket.svg"
        alt="..."
      />
      <p class="text-center mb-2">
        <strong>SB Admin Pro</strong> is packed with premium features,
        components, and more!
      </p>
      <a
        class="btn btn-success btn-sm"
        href="https://startbootstrap.com/theme/sb-admin-pro"
        >Upgrade to Pro!</a
      >
    </div> -->
  </ul>
  <!-- End of Sidebar -->
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters(["getLoginState"]),
  },
};
</script>

<style>
.nav-item {
  margin-top: 8px;
  margin-bottom: 8px;
  text-align: left;
}

.ll {
  color: white;
  margin-left: 16px;
}

.ll:hover {
  color: rgb(202, 200, 200);
  margin-left: 18px;
  text-decoration: none;
}
</style>
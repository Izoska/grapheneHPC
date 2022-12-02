
<template>
  <div id="page-top">
    <div id="wrapper">
      <!-- Page Wrapper -->
      <div id="content-wrapper" class="d-flex flex-column">
        <!-- Main Content -->
        <div id="content">
          <div>
            <div class="row mr-0">
              <navi-bar />
              <div class="col col-10">
                <top-bar />
                <router-view />
                <footer-bar />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NaviBar from "./components/layout/NaviBar.vue";
import TopBar from "./components/layout/TopBar.vue";
import FooterBar from "./components/layout/Footer.vue";

export default {
  components: {
    NaviBar,
    TopBar,
    FooterBar,
  },
};
</script>

<style>
@import url("/css/sb-admin-2.css");
</style>
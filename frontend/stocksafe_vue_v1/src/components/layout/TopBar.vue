
<template>
  <!-- Topbar -->
  <nav
    class="
      navbar navbar-expand navbar-light
      bg-white
      topbar
      mb-4
      static-top
      shadow
    "
  >
    <!-- Sidebar Toggle (Topbar) -->
    <button
      id="sidebarToggleTop"
      class="btn btn-link d-md-none rounded-circle mr-3"
    >
      <i class="fa fa-bars"></i>
    </button>

    <!-- Topbar Search -->
    <form
      class="
        d-none d-sm-inline-block
        form-inline
        mr-auto
        ml-md-3
        my-2 my-md-0
        mw-100
        navbar-search
      "
    >
      <form
        class="input-group"
        autocomplete="off"
        style="width: 300px; margin-left: 20px"
      >
        <Dropdown
          :options="search_list"
          v-on:selected="validateSelection"
          v-on:filter="getDropdownValues"
          :disabled="false"
          placeholder="검색.."
        >
        </Dropdown>
        <div class="input-group-append">
          <button
            class="btn btn-primary"
            type="button"
            @click="searching()"
            style="margin-right: 2px"
          >
            <b-icon
              class="searchicon"
              icon="search"
              style="font-size: 21px; font-color: white"
            ></b-icon>
          </button>
        </div>
      </form>
    </form>

    <!-- Topbar Navbar -->
    <ul class="navbar-nav ml-auto">
      <!-- Nav Item - Search Dropdown (Visible Only XS) -->
      <li class="nav-item dropdown no-arrow d-sm-none">
        <a
          class="nav-link dropdown-toggle"
          href="#"
          id="searchDropdown"
          role="button"
          data-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
        >
          <i class="fas fa-search fa-fw"></i>
        </a>
        <!-- Dropdown - Messages -->
        <div
          class="dropdown-menu dropdown-menu-right p-3 shadow animated--grow-in"
          aria-labelledby="searchDropdown"
        >
          <form class="form-inline mr-auto w-100 navbar-search">
            <div class="input-group">
              <input
                type="text"
                class="form-control bg-light border-0 small"
                placeholder="Search for..."
                aria-label="Search"
                aria-describedby="basic-addon2"
              />
              <div class="input-group-append">
                <button class="btn btn-primary" type="button">
                  <i class="fas fa-search fa-sm"></i>
                </button>
              </div>
            </div>
          </form>
        </div>
      </li>

      <span v-if="this.getLoginState">
        <b-icon
          class="person-fillicon"
          icon="person-fill"
          style="
            font-size: 30px;
            font-color: grey;
            margin-top: 5px;
            margin-right: 20px;
          "
        ></b-icon>
      </span>
      <span v-if="this.getLoginState">
        <div class="userNickDiv">
          <span class="userNickFont"
            ><b>{{ this.getName }}</b></span
          >
          <span> </span>
        </div>
      </span>
      <div v-else>
        <button class="btn btn-success">
          <router-link
            :to="{ name: 'UserJoin' }"
            style="color: white; text-decoration: none"
          >
            회원가입</router-link
          >
        </button>
      </div>

      <div class="topbar-divider d-none d-sm-block"></div>

      <!-- Nav Item - User Information -->
      <li>
        <div v-if="this.getLoginState === false">
          <button class="btn btn-primary">
            <router-link
              :to="{ name: 'UserLogin' }"
              style="color: white; text-decoration: none"
            >
              로그인</router-link
            >
          </button>
        </div>
        <div v-else>
          <button class="btn btn-danger" @click="Logout()">로그아웃</button>
        </div>
      </li>

      <!-- <li class="nav-item dropdown no-arrow">
        <div class="dropdown">
          <span>여기에 마우스를 올려보세요!</span>
          <div class="dropdown-content">
            <p>마우스를 올려야 나타나는 div 요소입니다!</p>
          </div>
        </div>
      </li> -->
    </ul>
  </nav>
</template>

<script>
import http from "@/utils/http-common.js";

import Dropdown from "vue-simple-search-dropdown";
import { mapMutations } from "vuex";
import { mapGetters } from "vuex";

export default {
  created() {
    console.log(this.getLoginState);

    this.getAlllist();
  },
  computed: {
    ...mapGetters([
      "getLoginState",
      "getName",
      "getNowPageStateLike",
      "getNowPageStateMy",
    ]),
  },
  components: { Dropdown },
  methods: {
    ...mapMutations(["SET_LOGOUT_STATE", "SET_TRUE_NOW_PAGE_STATE"]),
    Logout() {
      alert("로그아웃 합니다.");
      this.SET_LOGOUT_STATE();
    },
    validateSelection(selection) {
      this.selected = selection;
      console.log(selection.name + " has been selected");
    },

    getDropdownValues(keyword) {
      console.log(
        "You could refresh options by querying the API with " + keyword
      );
    },
    getAlllist() {
      http
        .get(`/stock/searchAll`, { params: { keyword: "%" } })
        .then(({ data }) => {
          console.log(data);
          data.forEach((element) => {
            let temp = { id: "", name: "" };
            temp.id = element.id;
            temp.name = element.id + "  |  " + element.stockName;
            this.search_list.push(temp);
          });
          console.log(this.search_list);
        });
    },
    searching() {
      this.SET_TRUE_NOW_PAGE_STATE(this.selected.id);

      var tag_like = false;
      if (this.getNowPageStateLike) tag_like = true;

      var tag_my = false;
      if (this.getNowPageStateMy) tag_my = true;

      this.$router
        .push({
          name: "StockDetail",
          params: {
            id: this.selected.id,
            star_tag: tag_like,
            myStock_tag: tag_my,
          },
        })
        .catch(() => {});
    },
  },
  data() {
    return {
      search_list: [],

      selected: { name: null, id: null },
    };
  },
};
</script>

<style>
.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;

  position: absolute;

  background-color: #f9f9f9;

  min-width: 160px;

  padding: 8px;

  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
}

.dropdown:hover .dropdown-content {
  display: block;
}

.userNickFont {
  font-family: Arial, Helvetica, sans-serif;
  text-align: center;
  font-size: 23px;
}

.userNickDiv {
  margin-top: 2px;
  text-align: center;
}
</style>
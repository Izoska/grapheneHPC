
<template>
  <!-- Page Wrapper -->
  <div class="container-fluid">
    <!-- Page Heading -->
    <h1 class="h3 mb-2 text-gray-800">주식 목록</h1>
    <p class="mb-4"></p>

    <!-- DataTales Example -->
    <div class="card shadow mb-4">
      <div class="card-header py-3">
        <h6 class="m-0 font-weight-bold text-primary">
          주식 목록
          <b-icon
            class="staricon2"
            icon="arrow-clockwise"
            variant="secondary"
            @click="renew()"
            style="font-size: 21px"
          ></b-icon>
        </h6>
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <list-table
            :data="search_list"
            :columns="columns"
            type="forStockList"
          >
          </list-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import http from "@/utils/http-common.js";
import { mapGetters } from "vuex";

import ListTable from "@/components/list/ListTable.vue";

export default {
  name: "ListStock",
  created() {
    console.log(this.$route.query);
    if (Object.keys(this.$route.query).length === 1) {
      http
        .get(`/stock/searchAll`, { params: { keyword: "%" } })
        .then(({ data }) => {
          console.log(data);
          this.search_list = data;
        });
    } else {
      http
        .get(`/stock/searchAllbyTag`, {
          params: this.$route.query,
        })
        .then(({ data }) => {
          console.log(data);
          this.search_list = data;
        });
    }
  },
  computed: {
    ...mapGetters(["getId"]),
  },
  data() {
    return {
      data: null,
      columns: ["종목코드", "종목명", "섹터", "산업"],
      search_list: [],
      stockdetailinfo: null,
    };
  },
  components: {
    ListTable,
  },
  methods: {
    renew() {
      http
        .get(`/stock/searchAll`, { params: { keyword: "%" } })
        .then(({ data }) => {
          console.log(data);
          this.search_list = data;
        });
    },
  },
};
</script>

<style></style>
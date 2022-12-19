<template>
  <!-- Page Wrapper -->
  <div class="container-fluid">
    <!-- Page Heading -->
    <h1 class="h3 mb-2 text-gray-800">내 주식 관리</h1>
    <p class="mb-4">
      보유한 주식을 확인합니다. facebook의 시계열 예측모델 Prophet을 이용한
      3일후의 예측 가격을 제공하나 참고용으로만 확인하십시오. <br />
      거래의 책임은 거래 당사자에게 있습니다.
      <a target="_blank" href="https://facebook.github.io/prophet/"
        >official Prophet documentation</a
      >.
    </p>

    <!-- DataTales Example -->
    <div class="card shadow mb-4">
      <div class="card-header py-3">
        <h6 class="m-0 font-weight-bold text-primary">내 주식 목록</h6>
      </div>
      <div class="card-body">
        <div class="table-responsive">
          <list-table :data="data" :columns="columns" type="five"> </list-table>
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
  name: "MyStock",
  created() {
    console.log(this.getId);
    http
      .get(`/memberstock`, { params: { memberId: this.getId } })
      .then((res) => {
        this.data = res.data;
      });
  },
  computed: {
    ...mapGetters(["getId"]),
  },
  data() {
    return {
      data: null,
      // 예측 가격을 3일, 1주일, 1달 단위로 여러개 보여줘도 될것같지만 이건 서버 비용을 고려해봐야
      columns: [
        "종목명",
        "어제 가격",
        "3일 뒤 예측가",
        "한달 뒤 예측가",
        "일년 뒤 예측가",
      ],
    };
  },
  components: {
    ListTable,
  },
  methods: {},
};
</script>

<style></style>

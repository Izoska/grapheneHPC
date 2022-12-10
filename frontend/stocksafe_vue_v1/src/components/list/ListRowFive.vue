
<template>
  <tr>
    <td>
      <a class="stockName" @click="goDetail()">
        <!-- <router-link :to="{ name: 'StockDetail', params: { no: no } }">{{
          subject
        }}</router-link> -->
        {{ stockName }}
      </a>
    </td>

    <td>{{ stockYesterday }}</td>
    <td>{{ predictDay }}</td>
    <td>{{ predictMonth }}</td>
    <td>{{ predictYear }}</td>
  </tr>
</template>

<script>
import moment from "moment";
import { mapGetters } from "vuex";
import { mapMutations } from "vuex";

export default {
  name: "BoardListRow",

  props: {
    id: Number,
    memberId: String,
    predictDay: Number,
    predictGraph: String,
    predictId: String,
    predictMonth: Number,
    predictYear: Number,
    stockName: String,
    stockYesterday: Number,
  },
  computed: {
    changeDateFormat() {
      return moment(new Date(this.regtime)).format("YY.MM.DD.");
    },
    ...mapGetters(["getNowPageStateLike", "getNowPageStateMy"]),
  },
  methods: {
    ...mapMutations(["SET_TRUE_NOW_PAGE_STATE"]),
    goDetail() {
      this.SET_TRUE_NOW_PAGE_STATE(this.predictId);
      console.log(this.predictId);

      var tag_like = false;
      if (this.getNowPageStateLike) tag_like = true;

      var tag_my = false;
      if (this.getNowPageStateMy) tag_my = true;

      this.$router
        .push({
          name: "StockDetail",
          params: {
            id: this.predictId,
            star_tag: tag_like,
            myStock_tag: tag_my,
          },
        })
        .catch(() => {});
    },
  },
};
</script>

<style>
.stockName:hover {
  cursor: pointer;
}
</style>
<template>
  <tr>
    <td>{{ id }}</td>
    <td>
      <a class="stockName" @click="goDetail()">
        <!-- <router-link :to="{ name: 'StockDetail', params: { no: no } }">{{
          subject
        }}</router-link> -->
        {{ stockName }}
      </a>
    </td>
    <td>{{ stockSector }}</td>
    <td>{{ stockIndustry }}</td>
  </tr>
</template>

<script>
import moment from "moment";
import { mapGetters } from "vuex";
import { mapMutations } from "vuex";

export default {
  name: "BoardListRow",

  props: {
    id: String,
    stockSector: String,
    stockIndustry: String,
    stockName: String,
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
      this.SET_TRUE_NOW_PAGE_STATE(this.id);

      var tag_like = false;
      if (this.getNowPageStateLike) tag_like = true;

      var tag_my = false;
      if (this.getNowPageStateMy) tag_my = true;

      this.$router
        .push({
          name: "StockDetail",
          params: {
            id: this.id,
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

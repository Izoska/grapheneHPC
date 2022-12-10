
<template>
  <table class="table" id="dataTable" width="100%" cellspacing="0">
    <thead>
      <tr>
        <th v-for="(column, idx) in columns" :key="idx">{{ column }}</th>
      </tr>
    </thead>
    <tbody v-if="type == 'five'">
      <list-row-five v-for="(item, index) in data" :key="index" v-bind="item" />
    </tbody>
    <tbody v-if="type == 'two'">
      <list-row-two v-for="(item, index) in data" :key="index" v-bind="item" />
    </tbody>
    <tbody v-if="type == 'forStockList'">
      <list-row-for-stock-list
        v-for="(item, index) in data"
        :key="index"
        v-bind="item"
      />
    </tbody>
  </table>
</template>

<script>
import ListRowTwo from "./ListRowTwo.vue";
import ListRowFive from "./ListRowFive.vue";
import ListRowForStockList from "./ListRowForStockList.vue";
export default {
  name: "ListTable",
  components: {
    ListRowFive,
    ListRowTwo,
    ListRowForStockList,
  },
  props: {
    data: [],
    columns: [],
    type: String,
  },
  data() {
    return {
      keyword: "",
    };
  },
  created() {},
  computed: {},
  watch: {},
  methods: {
    range(start, end) {
      if (!end) {
        end = start;
        start = 0;
      }
      start -= 1;
      // end -= 1;
      let arr = [];
      while (start++ !== end) {
        arr.push(start);
      }
      return arr;
    },
    movePage(idx) {
      this.paging.nowPage = idx;
    },
    previous() {
      if (this.paging.nowPage <= 5) {
        alert("더이상 앞으로 갈 수 없습니다.");
      } else {
        this.paging.nowPage = this.paging.startPage - 1;
        this.paging.startPage -= 5;
        this.paging.endPage -= 5;
      }
    },
    next() {
      this.paging.nowPage = this.paging.endPage + 1;
      this.paging.startPage += 5;
      this.paging.endPage += 5;
    },
  },
};
</script>

<style></style>
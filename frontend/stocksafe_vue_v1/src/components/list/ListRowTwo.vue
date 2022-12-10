<template>
  <tr>
    <div v-if="newsTitle">
      <td class="col-8">
        <a target="_blank" :href="newsUri">{{ newsTitle }}</a>
      </td>
      <td class="col-4"></td>
      <td class="col-2">{{ newsDate }}</td>
    </div>

    <div v-if="replyContent">
      <td>
        <div v-if="replyContent">{{ replyContent }}</div>
      </td>
      <td class="text-right col-4">{{ replyRegdate }}</td>
    </div>
  </tr>
</template>

<script>
import moment from "moment";

export default {
  name: "BoardListRow",
  props: {
    newsDate: String,
    newsTitle: String,
    newsUri: String,

    replyContent: String,
    replyRegdate: String,
  },
  computed: {
    changeDateFormat() {
      return moment(new Date(this.regtime)).format("YY.MM.DD.");
    },
  },
};
</script>

<style></style>

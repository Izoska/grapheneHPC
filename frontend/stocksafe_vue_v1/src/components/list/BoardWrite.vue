<template>
  <div class="d-flex flex-column">
    <main class="flex-shrink-0">
      <section class="py-5">
        <div class="container px-5 my-5">
          <div class="text-center mb-5">
            <div v-if="this.type === 'regist'">
              <h1 class="fw-bolder">문의 작성</h1>
            </div>
            <div v-else-if="this.type === 'notice'">
              <h1 class="fw-bolder">공지사항 작성</h1>
            </div>
            <div v-else>
              <h1 class="fw-bolder">문의 수정</h1>
            </div>
          </div>
          <form>
            <div class="form-floating mb-3">
              <div class="small text-uppercase fw-bold">제목</div>
              <input
                class="form-control"
                id="subject"
                type="text"
                v-model="article.subject"
                placeholder="Enter your id..."
                data-sb-validations="required"
              />
            </div>
            <div class="form-floating mb-3">
              <div class="small text-uppercase fw-bold">내용</div>
              <textarea
                class="form-control"
                id="message"
                type="text"
                placeholder="Enter your message here..."
                style="height: 10rem"
                v-model="article.content"
                data-sb-validations="required"
              ></textarea>
            </div>
            <a class="btn btn-primary float-right" @click="beforeSubmit"
              >완료</a
            >
          </form>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import { mapState } from "vuex";
const userStore = "userStore";
// import { getArticle } from "@/api/qna.js";

export default {
  name: "BoardWrite",
  props: {
    type: { type: String }, // regist or modify
    submit: Function,
    modiArticle: {},
  },
  created() {
    if (this.type === "modify") {
      this.article = this.modiArticle;
    }
  },
  data() {
    return {
      article: {
        no: null,
        userid: null,
        subject: null,
        content: null,
        hit: null,
        regtime: null,
        answer: null,
      },
    };
  },
  computed: {
    ...mapState(userStore, ["userInfo"]),
    setData() {
      return this.article;
    },
  },
  methods: {
    beforeSubmit() {
      this.article.userid = this.userInfo.userId;
      this.$emit("submit", this.article);
    },
    movePage() {
      this.$router.push({ name: "Login" });
    },
  },
};
</script>

<style></style>

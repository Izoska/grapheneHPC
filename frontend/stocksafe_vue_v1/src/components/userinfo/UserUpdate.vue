
<template>
  <form class="user">
    <div class="text-center">
      <h1 class="h4 text-gray-900 mb-4">Edit your info!</h1>
    </div>
    <div class="form-group">
      <input
        type="text"
        class="form-control form-control-user"
        id="id"
        placeholder="ID"
        readonly
        v-model="update_data.id"
      />
    </div>
    <div class="form-group row">
      <div class="col-sm-6 mb-3 mb-sm-0">
        <input
          type="password"
          class="form-control form-control-user"
          id="exampleInputPassword"
          placeholder="Password"
          v-model="update_data.member_pw"
        />
      </div>
      <div class="col-sm-6">
        <input
          type="password"
          class="form-control form-control-user"
          id="exampleRepeatPassword"
          placeholder="Repeat Password"
        />
      </div>
    </div>
    <div class="form-group row">
      <div class="col-sm-6 mb-3 mb-sm-0">
        <input
          type="text"
          class="form-control form-control-user"
          id="firstName"
          placeholder="Nick Name"
          v-model="update_data.member_name"
        />
      </div>
    </div>
    <div class="form-group row">
      <div class="col-sm-6 mb-3 mb-sm-0">
        <input
          type="text"
          class="form-control form-control-user"
          id="exampleFirstName"
          placeholder="email"
          v-model="update_data.member_email_id"
        />
      </div>
      @
      <div class="col-sm-6">
        <input
          type="text"
          class="form-control form-control-user"
          id="exampleLastName"
          placeholder="email domain"
          v-model="update_data.member_email_domain"
        />
      </div>
    </div>
    <button class="btn btn-primary btn-user btn-block" @click="UpdateUser">
      Update Account
    </button>
    <hr />
  </form>
</template>

<script>
import http from "@/utils/http-common.js";
import { mapGetters } from "vuex";

export default {
  name: "UserUpdate",
  created() {
    this.update_data.id = this.getId;
    this.getUserInfo();
  },
  components: {},
  computed: {
    ...mapGetters(["getId"]),
  },
  data() {
    return {
      update_data: {
        id: "",
        member_pw: "",
        member_name: "",
        member_email_id: "",
        member_email_domain: "",
      },
    };
  },
  methods: {
    UpdateUser() {
      http
        .put(`/member/edit`, {
          id: this.update_data.id,
          memberPw: this.update_data.member_pw,
          memberName: this.update_data.member_name,
          memberEmailId: this.update_data.member_email_id,
          memberEmailDomain: this.update_data.member_email_domain,
        })
        .then(({ data }) => {
          console.log(data);
          let msg = "회원수정 실패.";
          if (data != "") {
            msg = "회원수정 성공";
            alert(msg);
            this.$router.push({ name: "Home" });
          } else alert(msg);
        });
    },
    getUserInfo() {
      http
        .get(`/member`, { params: { id: this.update_data.id } })
        .then(({ data }) => {
          console.log(data);
          this.update_data.member_pw = data.memberPw;
          this.update_data.member_name = data.memberName;
          this.update_data.member_email_id = data.memberEmailId;
          this.update_data.member_email_domain = data.memberEmailDomain;
        });
    },
  },
};
</script>

<style></style>
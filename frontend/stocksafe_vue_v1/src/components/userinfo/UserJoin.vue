
<template>
  <form class="user">
    <div class="text-center">
      <h1 class="h4 text-gray-900 mb-4">Welcome!</h1>
    </div>
    <div class="form-group">
      <input
        type="text"
        class="form-control form-control-user"
        id="id"
        placeholder="ID"
        v-model="singup_data.id"
      />
    </div>
    <div class="form-group row">
      <div class="col-sm-6 mb-3 mb-sm-0">
        <input
          type="password"
          class="form-control form-control-user"
          id="exampleInputPassword"
          placeholder="Password"
          v-model="singup_data.member_pw"
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
          v-model="singup_data.member_name"
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
          v-model="singup_data.member_email_id"
        />
      </div>
      @
      <div class="col-sm-6">
        <input
          type="text"
          class="form-control form-control-user"
          id="exampleLastName"
          placeholder="email domain"
          v-model="singup_data.member_email_domain"
        />
      </div>
    </div>

    <button class="btn btn-primary btn-user btn-block" @click="SignUp()">
      Register Account
    </button>
    <hr />
    <a href="index.html" class="btn btn-google btn-user btn-block">
      <i class="fab fa-google fa-fw"></i> Register with Google
    </a>
    <a href="index.html" class="btn btn-facebook btn-user btn-block">
      <i class="fab fa-facebook-f fa-fw"></i> Register with Facebook
    </a>
  </form>
</template>

<script>
import http from "@/utils/http-common.js";

export default {
  data() {
    return {
      singup_data: {
        id: "",
        member_pw: "",
        member_name: "",
        member_email_id: "",
        member_email_domain: "",
      },
    };
  },
  methods: {
    SignUp() {
      http
        .post(`/member/signup`, {
          id: this.singup_data.id,
          memberPw: this.singup_data.member_pw,
          memberName: this.singup_data.member_name,
          memberEmailId: this.singup_data.member_email_id,
          memberEmailDomain: this.singup_data.member_email_domain,
        })
        .then(({ data }) => {
          console.log(data);
          let msg = "회원가입 실패.";
          if (data != "") {
            msg = "회원가입 성공";
            alert(msg);
            this.$router.push({ name: "Home" });
          } else alert(msg);
        });
    },
  },
};
</script>

<style></style>
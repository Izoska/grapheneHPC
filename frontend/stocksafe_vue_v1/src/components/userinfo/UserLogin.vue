<template>
  <div class="user">
    <div class="text-center">
      <h1 class="h4 text-gray-900 mb-4">Welcome Back!</h1>
    </div>
    <div class="form-group">
      <input
        type="text"
        class="form-control form-control-user"
        id="exampleInputEmail"
        aria-describedby="emailHelp"
        placeholder="Enter Email Address..."
        v-model="login_user.id"
      />
    </div>
    <div class="form-group">
      <input
        type="password"
        class="form-control form-control-user"
        id="exampleInputPassword"
        placeholder="Password"
        v-model="login_user.pw"
      />
    </div>
    <div class="form-group">
      <div class="custom-control custom-checkbox small">
        <input type="checkbox" class="custom-control-input" id="customCheck" />
        <label class="custom-control-label" for="customCheck"
          >Remember Me</label
        >
      </div>
    </div>
    <button class="btn btn-primary btn-user btn-block" @click="Login()">
      Login
    </button>
    <hr />
    <a href="index.html" class="btn btn-google btn-user btn-block">
      <i class="fab fa-google fa-fw"></i> Login with Google
    </a>
    <a href="index.html" class="btn btn-facebook btn-user btn-block">
      <i class="fab fa-facebook-f fa-fw"></i> Login with Facebook
    </a>
    <hr />
    <div class="text-center">
      <router-link class="small" :to="{ name: 'UserPassword' }"
        >Forgot Password?</router-link
      >
    </div>
    <div class="text-center">
      <rout
<template>
  <div class="d-flex flex-column">
    <main class="flex-shrink-0">
      <section class="py-5">
        <div class="container px-5 my-5">
          <div class="text-center mb-5">
            <div v-if="this.type === 'regist'">
              <h1 class="fw-bolder">문의 작성</h1>
            </div>
            <div v-else-if="this.type =
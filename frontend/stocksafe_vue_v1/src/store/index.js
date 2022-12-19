
import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    login_state: false,
    user_id : "",
    user_name: "",
    like_stock: {},
    nasdaq_like_stock: [],
    my_stock: {},
    nasdaq_my_stock:[],
    now_page_state_like: false,
    now_page_state_my: false,
  },
  mutations: {
    SET_LOGIN_STATE(state, data) {
      state.login_state = true;
      state.user_id = data.id;
      state.user_name = data.name;
    },
    SET_LOGOUT_STATE(state) {
      state.login_state = false;
      state.user_id = null;
      state.user_name = null;
    },
    SET_LIKE_STOCK(state, data) {
      let arr = new Object();
      
      state.like_stock = data;
      
      state.like_stock.forEach(element => {
        arr[element.predictId] = 1;
      });

      state.nasdaq_like_stock = arr;
    },
    SET_MY_STOCK(state, data) {
      let arr = new Object();
      
      state.my_stock = data;
      
      state.my_stock.forEach(element => {
        arr[element.predictId] = 1;
      });

      state.nasdaq_my_stock = arr;
    },
    SET_TRUE_NOW_PAGE_STATE(state, id) {

      if(state.nasdaq_like_stock[id] === 1) state.now_page_state_like = true;
      else state.now_page_state_like = false;
      
      if(state.nasdaq_my_stock[id] === 1) state.now_page_state_my = true;
      else state.now_page_state_my = false;
      
    },
    SET_FALSE_NOW_PAGE_STATE(state) {
      state.now_page_state_like = false;
      state.now_page_state_my = false;
    },
    SET_INDEX_LIKE_STOCK(state, id) {
      if (state.nasdaq_like_stock[id] == 1) {
        state.nasdaq_like_stock[id] = 0;
      }
      else state.nasdaq_like_stock[id] = 1;
    },
    SET_INDEX_MY_STOCK(state, id) {
      if (state.nasdaq_my_stock[id] == 1) {
        state.nasdaq_my_stock[id] = 0;
      }
      else state.nasdaq_my_stock[id] = 1;
    },
    
  },
  getters: {
    getLoginState(state) {
      return state.login_state;
    },
    getName(state) {
      return state.user_name;
    },
    getId(state) {
      return state.user_id;
    },
    getNowPageStateLike(state) {
      return state.now_page_state_like;
    },
    getNowPageStateMy(state) {
      return state.now_page_state_my;
    },
    
  },
  actions: {
    
  },
  modules: {},
  plugins: [createPersistedState()],
});
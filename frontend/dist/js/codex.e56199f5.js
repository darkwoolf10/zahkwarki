(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["codex"],{"43f1":function(e,t,s){"use strict";s.r(t);var n=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"home wrapper"},[s("Sidebar",{attrs:{users:e.users}}),s("div",{attrs:{id:"content"}},[s("Header",{attrs:{users:e.users,login:e.login}}),e._m(0)],1)],1)},a=[function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"row"},[s("h1",[e._v("This is an codex page")])])}],r=s("54b9"),i=r["a"],o=s("2877"),c=Object(o["a"])(i,n,a,!1,null,"5223fb77",null);t["default"]=c.exports},"54b9":function(e,t,s){"use strict";(function(e){s("cadf"),s("551c"),s("097d");var n=s("0418"),a=s("5ea5");t["a"]={name:"Codex",data:function(){return{users:!1,login:!0}},components:{Header:n["a"],Sidebar:a["a"]},mounted:function(){e(document).ready(function(){e("#sidebarCollapse").on("click",function(){e("#sidebar").toggleClass("active")})})},created:function(){var t=this;e.ajax({url:this.$store.state.url_server+"api/users/",type:"GET",headers:{Authorization:"Token "+sessionStorage.getItem("token")},success:function(e){t.users=e,t.login=!1}})}}}).call(this,s("1157"))}}]);
//# sourceMappingURL=codex.e56199f5.js.map
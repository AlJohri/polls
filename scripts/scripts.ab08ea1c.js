"use strict";angular.module("pollsApp",["ngAnimate","ngCookies","ngResource","ngRoute","ngSanitize","ngTouch","firebase","firebase.ref"]),angular.module("pollsApp").controller("HeaderCtrl",["$scope","Ref","$location",function(a,b,c){a.isActive=function(a){return a===c.path()}}]),angular.module("pollsApp").controller("HPCtrl",["$scope","Ref","$firebaseArray","$timeout","$http","$q",function(a,b,c,d,e,f){function g(b){a.err=b,d(function(){a.err=null},5e3)}a.hp=c(b.child("hp")),a.hp.$loaded()["catch"](g),a.refreshHP=function(){e.get("http://todayspolls.herokuapp.com/hp")}}]),angular.module("pollsApp").controller("RCPCtrl",["$scope","Ref","$firebaseArray","$timeout","$http","$q",function(a,b,c,d,e,f){function g(b){a.err=b,d(function(){a.err=null},5e3)}a.rcp=c(b.child("rcp")),a.rcp.$loaded()["catch"](g),a.refreshRCP=function(){e.get("http://todayspolls.herokuapp.com/rcp")}}]),angular.module("pollsApp").controller("QuinnipiacCtrl",["$scope","Ref","$firebaseArray","$timeout","$http","$q",function(a,b,c,d,e,f){function g(b){a.err=b,d(function(){a.err=null},5e3)}a.quinnipiac=c(b.child("quinnipiac")),a.quinnipiac.$loaded()["catch"](g),a.refreshQuinnipiac=function(){e.get("http://todayspolls.herokuapp.com/quinnipiac")}}]),angular.module("firebase.config",[]).constant("FBURL","https://aljohri-polls.firebaseio.com"),angular.module("firebase.ref",["firebase","firebase.config"]).factory("Ref",["$window","FBURL",function(a,b){return new a.Firebase(b)}]),angular.module("pollsApp").controller("ChatCtrl",["$scope","Ref","$firebaseArray","$timeout",function(a,b,c,d){function e(b){a.err=b,d(function(){a.err=null},5e3)}a.messages=c(b.child("messages").limitToLast(10)),a.messages.$loaded()["catch"](e),a.addMessage=function(b){b&&a.messages.$add({text:b})["catch"](e)}}]),angular.module("pollsApp").filter("reverse",function(){return function(a){return angular.isArray(a)?a.slice().reverse():[]}}),angular.module("pollsApp").filter("join",function(){return function(a,b){return(a||[]).join(b)}}),angular.module("pollsApp").filter("pluck",function(){return function(a,b){return _.pluck(a,b)}}),angular.module("pollsApp").filter("pluck2",function(){return function(a,b,c){return _.chain(a).map(function(a){return _.pick(a,[b,c])}).map(function(a){return a[b]+": "+a[c]+"%"}).flatten().value()}}),angular.module("pollsApp").config(["$routeProvider",function(a){a.when("/",{templateUrl:"views/main.html"}).when("/rcp",{templateUrl:"views/rcp.html",controller:"RCPCtrl"}).when("/hp",{templateUrl:"views/hp.html",controller:"HPCtrl"}).when("/quinnipiac",{templateUrl:"views/quinnipiac.html",controller:"QuinnipiacCtrl"}).otherwise({redirectTo:"/"})}]);
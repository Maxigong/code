import Vue from 'vue';
import VueRouter from 'vue-router';
import CaptureImg from '../views/CaptureImg.vue';
import Contact from '../views/Contact.vue';
import Home from '../views/Home.vue';
import SVGPath from '../views/SVGPath.vue';
import SVGPath2 from '../views/SVGPath2.vue';
import Dashboard from '../views/Dashboard.vue';
import BlogPage from '../views/BlogPage.vue';
import Post from '../views/Post.vue';

// Stadel

import StadelWelcome from '../views/Stadel/StadelWelcome';
import DiscoverPaint from '../views/Stadel/DiscoverPaint';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/svg-path',
    name: 'SVGPath',
    component: SVGPath,
  },
  {
    path: '/svg-path-2',
    name: 'SVGPath2',
    component: SVGPath2,
  },
  {
    path: '/capture-img',
    name: 'CaptureImg',
    component: CaptureImg,
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact,
  },
  {
    path: '/Dashboard',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    // path: '/post',
    path: '/post/:slug',
    name: 'post',
    component: Post,
  },
  {
    path: '/blog',
    name: 'blog',
    component: BlogPage,
  },

  // stadel
  {
    path: '/welcome',
    name: 'StadelWelcome',
    component: StadelWelcome,
  },
  {
    path: '/painting',
    name: 'DiscoverPaint',
    component: DiscoverPaint,
  },
];
const router = new VueRouter({
  routes,
});

export default router;

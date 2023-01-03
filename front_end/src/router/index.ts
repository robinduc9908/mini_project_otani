import Vue from 'vue'
import VueRouter, {RouteConfig} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginVue from "@/components/LoginVue.vue";
import HomeVue from "@/components/HomeVue.vue";
import TopBar from "@/components/TopBar.vue";
import Menu from "@/components/Menu.vue";
import Sidebar from "@/components/Sidebar.vue";
import Caroulsels from "@/components/caroulsels.vue";
import productItem from "@/components/productItem.vue";
import FootballClothesView from "@/views/FootballClothesView.vue";
import FootballShoesView from "@/views/FootballShoesView.vue";
import SportEquipmentView from "@/views/SportEquipmentView.vue";
import userManagement from "@/components/UserManagement.vue";
import UserManagementView from "@/views/UserManagementView.vue";
import productItemUser from "@/components/productItemUser.vue";
import Add from "@/components/Add.vue";
import productDetail from "@/components/productDetail.vue";
import Cart from "@/components/Cart.vue";
import CartView from "@/views/CartView.vue";
import Edit from "@/components/Edit.vue";


Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },

    {
        path: '/login',
        name: 'login',
        component: LoginVue
    },
    {
        path: '/topbar',
        name: 'topbar',
        component: TopBar
    },
    {
        path: '/cartview',
        name: 'carview',
        component: CartView
    },
    {
        path: '/productItems',
        name: 'productitems',
        component: productItem
    },
    {
        path: '/productDetail',
        name: 'productdetail',
        component: productDetail
    },

    {
        path: '/productItem/{id}',
        name: 'productitem',
        component: () => import('../views/ProductDetail.vue')
    },
    {
        path: '/editItem/{id}',
        name: 'editItem',
        component: () => import('../components/Edit.vue')
    },
    {
        path: '/footballclothes',
        name: 'footballclothes',
        component: FootballClothesView
    },
    {
        path: '/footballshoes',
        name: 'footballshoes',
        component: FootballShoesView
    },
    {
        path: '/sportequipment',
        name: 'sportequipment',
        component: SportEquipmentView
    },
    {
        path: '/user',
        name: 'user',
        component: UserManagementView
    },

    {
        path: '/productItemUser',
        name: 'producItemUser',
        component: productItemUser
    },
    {
        path: '/add',
        name: 'Add',
        component: Add
    },
    {
        path: '/edit',
        name: 'Edit',
        component: Edit
    },
    {
        path: '/cart',
        name: 'Cart',
        component: Cart
    }

]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router

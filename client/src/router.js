import { createMemoryHistory, createRouter } from 'vue-router'
import HomeView from './components/pages/HomeView.vue'
import EditionView from './components/pages/EditionView.vue'
import ReponseView from './components/pages/ReponseView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
   },
  {
    path: '/edition',
    name: 'edition',
    component: EditionView
   },
  {
    path: '/reponse',
    name: 'reponse',
    component: ReponseView
   },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router

import { createMemoryHistory, createRouter } from 'vue-router'

import EditionView from './components/pages/EditionView.vue'
import ReponseView from './components/pages/ReponseView.vue'

const routes = [
    { path: '/', component: HomeView },
    { path: '/edition', component: EditionView },
    { path: '/reponse', component: ReponseView },
]
const router = createRouter({
    history: createMemoryHistory(),
    routes,
})
export default router
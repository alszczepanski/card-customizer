/* eslint-disable */

import { defineStore } from "pinia";

const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        user: { id: '1', username: 'testowy'},
    }),
    actions: {
        async login(username, _password) {
            const user = { id: '1', username }
            localStorage.setItem('user', JSON.stringify(user));
        },
        logout() {
            this.user = null;
            localStorage.removeItem('user');
        }
    }
});

export default useAuthStore;
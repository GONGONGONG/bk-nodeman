<template>
  <bk-dropdown-menu
    ref="dropdownRef"
    :trigger="trigger"
    :font-size="fontSize"
    :disabled="disabled"
    @show="showDropdown = true"
    @hide="showDropdown = false">
    <bk-button
      :ext-cls="extCls"
      slot="dropdown-trigger"
      :theme="theme"
      :loading="loading"
      :disabled="disabled"
      v-test.common="`more.${testKey}`">
      <span class="icon-down-wrapper">
        {{ btnText }}
        <i v-if="showIcon" :class="['bk-icon icon-angle-down setup-btn-icon', { 'icon-flip': showDropdown }]"></i>
      </span>
    </bk-button>
    <ul class="bk-dropdown-list" slot="dropdown-content">
      <li v-for="menu in menuList" :key="menu.id">
        <a
          href="javascript:"
          :class="{ 'item-disabled': menu.disabled }"
          v-test.common="`moreItem.${menu.id}`"
          @click.prevent.stop="menuItemClick(menu)">
          {{ menu.name }}
        </a>
      </li>
    </ul>
  </bk-dropdown-menu>
</template>

<script lang="ts">
import { Vue, Component, Prop, Emit, Ref } from 'vue-property-decorator';
import { IDropdownItem } from '@/types';

@Component({ name: 'BtnDropdown' })

export default class BtnDropdown extends Vue {
  @Prop({ type: String, default: 'click' }) private readonly trigger!: string;
  @Prop({ type: Boolean, default: false }) private readonly disabled!: boolean;
  @Prop({ type: Boolean, default: true }) private readonly prevent!: boolean; // 点击收起下拉
  @Prop({ type: Boolean, default: true }) private readonly showIcon!: boolean;
  @Prop({ type: Boolean, default: false }) private readonly loading!: boolean;
  @Prop({ type: Array, default: () => [] }) private readonly menuList!: IDropdownItem[];
  @Prop({ type: String, default: 'default' }) private readonly theme!: string;
  @Prop({ type: String, default: 'medium' }) private readonly fontSize!: string;
  @Prop({ type: String, default: '' }) private readonly btnText!: string;
  @Prop({ type: String, default: '' }) private readonly extCls!: string;
  @Prop({ type: String, default: '' }) private readonly testKey!: string;

  @Ref('dropdownRef') private readonly dropdownRef!: any;

  private showDropdown = false;

  @Emit('menu-click')
  public handleClick(menu: IDropdownItem) {
    return menu;
  }

  public menuItemClick(menu: IDropdownItem) {
    if (!menu.disabled) {
      this.handleClick(menu);
      if (this.prevent) {
        this.hide();
      }
    }
  }
  public show() {
    this.dropdownRef.show();
  }
  public hide() {
    this.dropdownRef.hide();
  }
}
</script>

<style lang="postcss" scoped>
  .icon-down-wrapper {
    position: relative;
    left: 3px;
  }
  .bk-dropdown-list .item-disabled {
    cursor: not-allowed;
    color: #c4c6cc;
    &:hover {
      color: #c4c6cc;
    }
  }
</style>

DROP TABLE IF EXISTS  SECFORT_JK_POLICY_USER_REL;
DROP TABLE IF EXISTS  SECFORT_JK_POLICY_APPROVALUSER_REL;
DROP TABLE IF EXISTS secfort_jk_rule;

DROP TABLE IF EXISTS secfort_jk_apply;
DROP TABLE IF EXISTS secfort_jk_policy;

CREATE TABLE secfort_jk_apply(
    uuid VARCHAR(32) NOT NULL,
    apply_id VARCHAR(60),
    session_id VARCHAR(32),
    user_ip VARCHAR(32),
    user_id VARCHAR(32),
    res_id VARCHAR(32),
    res_ip VARCHAR(32),
    res_port VARCHAR(60),
    res_account VARCHAR(60),
    policy_id VARCHAR(60),
    sensitive_cmd TEXT,
    sensitive_rule TEXT,
    auth_mode VARCHAR(60),
    user_times VARCHAR(60),
    used_times VARCHAR(60),
    duration VARCHAR(60),
    selected_approver VARCHAR(60),
    create_time VARCHAR(60),
    apply_reason VARCHAR(60),
    approval_reason VARCHAR(60),
    apply_status VARCHAR(60),
    PRIMARY KEY (uuid)
);

COMMENT ON TABLE secfort_jk_apply IS '金库申请表';
COMMENT ON COLUMN secfort_jk_apply.uuid IS '主键ID';
COMMENT ON COLUMN secfort_jk_apply.apply_id IS '申请id';
COMMENT ON COLUMN secfort_jk_apply.session_id IS '会话ID';
COMMENT ON COLUMN secfort_jk_apply.user_ip IS '用户IP地址';
COMMENT ON COLUMN secfort_jk_apply.user_id IS '主账号';
COMMENT ON COLUMN secfort_jk_apply.res_id IS '资源ID';
COMMENT ON COLUMN secfort_jk_apply.res_ip IS '资源IP';
COMMENT ON COLUMN secfort_jk_apply.res_port IS '资源端口';
COMMENT ON COLUMN secfort_jk_apply.res_account IS '从账号';
COMMENT ON COLUMN secfort_jk_apply.policy_id IS '策略ID';
COMMENT ON COLUMN secfort_jk_apply.sensitive_cmd IS '执行的敏感指令';
COMMENT ON COLUMN secfort_jk_apply.sensitive_rule IS '匹配到的敏感策略规则';
COMMENT ON COLUMN secfort_jk_apply.auth_mode IS '认证方式';
COMMENT ON COLUMN secfort_jk_apply.user_times IS '申请次数';
COMMENT ON COLUMN secfort_jk_apply.used_times IS '使用次数（默认0，触发+1，==申请次数=失效）';
COMMENT ON COLUMN secfort_jk_apply.duration IS '申请时长（2小时：当前时间>创建时间+2小时=过期）';
COMMENT ON COLUMN secfort_jk_apply.selected_approver IS '审批人信息';
COMMENT ON COLUMN secfort_jk_apply.create_time IS '申请创建时间';
COMMENT ON COLUMN secfort_jk_apply.apply_reason IS '申请理由';
COMMENT ON COLUMN secfort_jk_apply.approval_reason IS '审批原因';
COMMENT ON COLUMN secfort_jk_apply.apply_status IS '申请状态';



CREATE TABLE secfort_jk_policy(
    uuid VARCHAR(32) NOT NULL,
    policy_name VARCHAR(60),
    control_way VARCHAR(60),
    control_type VARCHAR(60),
    user_times VARCHAR(60),
    duration VARCHAR(60),
    create_time VARCHAR(60),
    first_trigger VARCHAR(60),
    trigger_times int4(60),
    PRIMARY KEY (uuid)
);

COMMENT ON TABLE secfort_jk_policy IS '金库策略表';
COMMENT ON COLUMN secfort_jk_policy.uuid IS 'ID;金库策略主键UUID';
COMMENT ON COLUMN secfort_jk_policy.policy_name IS '策略名称';
COMMENT ON COLUMN secfort_jk_policy.control_way IS '管控方式';
COMMENT ON COLUMN secfort_jk_policy.control_type IS '管控类型;命令[ssh_proxy]、文件[ftp_proxy、webFTP]、SQL[db_proxy、webDB]] 数据库表结构';
COMMENT ON COLUMN secfort_jk_policy.user_times IS '申请方式次数;SECOND_1/HOUR_1';
COMMENT ON COLUMN secfort_jk_policy.duration IS '申请方式小时';
COMMENT ON COLUMN secfort_jk_policy.create_time IS '创建时间';
COMMENT ON COLUMN secfort_jk_policy.first_trigger IS '第一次触发时间;审计报表统计命中策略数';
COMMENT ON COLUMN secfort_jk_policy.trigger_times IS '策略触发次数;统计命中低的策略';



CREATE TABLE secfort_jk_rule(
    uuid VARCHAR(32) NOT NULL,
    policy_uuid VARCHAR(32),
    rule VARCHAR(1000),
    PRIMARY KEY (uuid)
);

COMMENT ON TABLE secfort_jk_rule IS '金库规则表';
COMMENT ON COLUMN secfort_jk_rule.uuid IS '规则UUID';
COMMENT ON COLUMN secfort_jk_rule.policy_uuid IS '策略UUID';
COMMENT ON COLUMN secfort_jk_rule.rule IS '规则';

DROP TABLE IF EXISTS secfort_jk_policy_resource_rel;
CREATE TABLE secfort_jk_policy_resource_rel(
    uuid VARCHAR(32) NOT NULL,
    vault_policy_uuid VARCHAR(32),
    resource_uuid VARCHAR(32),
    PRIMARY KEY (uuid)
);

COMMENT ON TABLE secfort_jk_policy_resource_rel IS '金库策略-资源-关系表';
COMMENT ON COLUMN secfort_jk_policy_resource_rel.uuid IS '关联UUID';
COMMENT ON COLUMN secfort_jk_policy_resource_rel.vault_policy_uuid IS '策略UUID';
COMMENT ON COLUMN secfort_jk_policy_resource_rel.resource_uuid IS '资产UUID';

CREATE TABLE  SECFORT_JK_POLICY_APPROVALUSER_REL (
  UUID VARCHAR(32) NOT NULL,
  VAULT_POLICY_UUID VARCHAR(32),
  USER_UUID VARCHAR(32)
)
;
COMMENT ON COLUMN  SECFORT_JK_POLICY_APPROVALUSER_REL.UUID IS '金库策略与审批人关系表主键UUID';
COMMENT ON COLUMN  SECFORT_JK_POLICY_APPROVALUSER_REL.VAULT_POLICY_UUID IS '金库策略ID';
COMMENT ON COLUMN  SECFORT_JK_POLICY_APPROVALUSER_REL.USER_UUID IS '审批人ID';
ALTER TABLE  SECFORT_JK_POLICY_APPROVALUSER_REL ADD CONSTRAINT SECFORT_VAULT_COMMAND_COPY1_PKEY PRIMARY KEY (UUID);
ALTER TABLE  SECFORT_JK_POLICY_APPROVALUSER_REL ADD CONSTRAINT JK_STRATEGY_CASCADE FOREIGN KEY (VAULT_POLICY_UUID) REFERENCES  SECFORT_JK_POLICY (UUID) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE  SECFORT_JK_POLICY_USER_REL (
  UUID VARCHAR(32) NOT NULL,
  VAULT_POLICY_UUID VARCHAR(32),
  USER_UUID VARCHAR(32)
)
;
COMMENT ON COLUMN  SECFORT_JK_POLICY_USER_REL.UUID IS '金库策略与用户关系表主键UUID';
COMMENT ON COLUMN  SECFORT_JK_POLICY_USER_REL.VAULT_POLICY_UUID IS '金库策略ID';
COMMENT ON COLUMN  SECFORT_JK_POLICY_USER_REL.USER_UUID IS '用户ID';
ALTER TABLE  SECFORT_JK_POLICY_USER_REL ADD CONSTRAINT SECFORT_VAULT_COMMAND_COPY2_PKEY PRIMARY KEY (UUID);
ALTER TABLE  SECFORT_JK_POLICY_USER_REL ADD CONSTRAINT JK_STRATEGY_CASCADE FOREIGN KEY (VAULT_POLICY_UUID) REFERENCES  SECFORT_JK_POLICY (UUID) ON DELETE CASCADE ON UPDATE CASCADE;

